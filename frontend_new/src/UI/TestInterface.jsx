import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TestInterface = ({ sessionId, testId }) => {
    const [currentQues, setCurrentQues] = useState(1);
    const [questionData, setQuestionData] = useState(null);
    const [selectedAnswer, setSelectedAnswer] = useState('');
    const [submitStatus, setSubmitStatus] = useState('');
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const loadQuestion = async () => {
            setIsLoading(true);
            try {
                const response = await axios.get(
                    `http://localhost:8000/api/question/${testId}/${currentQues}/`,
                    {
                        headers: {
                            'X-Session-Id': sessionId
                        }
                    }
                );

                setQuestionData(response.data);
                setSelectedAnswer(response.data.current_answer || '');
                setSubmitStatus('');
            } catch (error) {
                console.error('Ошибка загрузки вопроса:', error);
                setSubmitStatus('Ошибка загрузки вопроса');
            } finally {
                setIsLoading(false);
            }
        };

        if (sessionId) {
            loadQuestion();
        }
    }, [testId, currentQues, sessionId]);

    const handleAnswerSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post(
                `http://localhost:8000/api/save-answer/${testId}/${currentQues}/`,
                {
                    answer_text: selectedAnswer,
                    session_id: sessionId
                },
                {
                    headers: {
                        'X-Session-Id': sessionId
                    }
                }
            );

            setSubmitStatus('Ответ успешно сохранен!');
            setTimeout(() => setSubmitStatus(''), 3000);

            // Автоматический переход к следующему вопросу
            if (questionData?.navigation?.next) {
                setCurrentQues(prev => prev + 1);
            }
        } catch (error) {
            console.error('Ошибка сохранения ответа:', error);
            setSubmitStatus('Ошибка сохранения ответа!');
        }
    };

    if (isLoading) {
        return <div className="loading">Загрузка вопроса...</div>;
    }

    if (!questionData) {
        return <div className="error">Не удалось загрузить вопрос</div>;
    }

    return (
        <div className="test-interface">
            <div className="progress-info">
                Вопрос {currentQues} из {questionData.navigation.total}
                <div className="progress-bar">
                    <div
                        className="progress-fill"
                        style={{ width: `${(currentQues / questionData.navigation.total) * 100}%` }}
                    />
                </div>
            </div>

            <form onSubmit={handleAnswerSubmit}>
                <div className="question-card">
                    <h3 className="question-text">
                        {questionData.question.question_text}
                    </h3>

                    <div className="answer-options">
                        {questionData.options.map(option => (
                            <label
                                key={option.id_answ}
                                className={`option-item ${
                                    selectedAnswer === option.answer_text ? 'selected' : ''
                                }`}
                            >
                                <input
                                    type="radio"
                                    name="answer"
                                    value={option.answer_text}
                                    checked={selectedAnswer === option.answer_text}
                                    onChange={(e) => setSelectedAnswer(e.target.value)}
                                    disabled={isLoading}
                                />
                                <span className="option-label">
                                    {option.answer_text}
                                </span>
                            </label>
                        ))}
                    </div>
                </div>

                <div className="navigation-controls">
                    <button
                        type="button"
                        className="nav-button prev-button"
                        disabled={!questionData.navigation.previous || isLoading}
                        onClick={() => setCurrentQues(prev => prev - 1)}
                    >
                        ← Назад
                    </button>

                    <button
                        type="submit"
                        className="submit-button"
                        disabled={isLoading}
                    >
                        {isLoading ? 'Сохранение...' : 'Сохранить ответ'}
                    </button>

                    <button
                        type="button"
                        className="nav-button next-button"
                        disabled={!questionData.navigation.next || isLoading}
                        onClick={() => setCurrentQues(prev => prev + 1)}
                    >
                        Далее →
                    </button>
                </div>

                {submitStatus && (
                    <div className={`status-message ${
                        submitStatus.includes('успешно') ? 'success' : 'error'
                    }`}>
                        {submitStatus}
                    </div>
                )}
            </form>
        </div>
    );
};

export default TestInterface;