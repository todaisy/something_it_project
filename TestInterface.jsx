import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TestInterface = ({ testId }) => {
    const [currentQues, setCurrentQues] = useState(1);
    const [questionData, setQuestionData] = useState(null);
    const [selectedAnswer, setSelectedAnswer] = useState('');
    const [submitStatus, setSubmitStatus] = useState('');

    const saveAnswer = async (answerData) => {
        await axios.post(`/api/questions/${sessionId}/2/${currentQuestion}/`, {
            ...answerData,
            id_test: 2,
            id_ques: currentQuestion
        });
    };

    useEffect(() => {
        const loadQuestion = async () => {
            try {
                const response = await axios.get(
                    `http://localhost:8000/api/questions/${testId}/${currentQues}/`
                );
                setQuestionData(response.data);
                setSelectedAnswer(response.data.current_answer || '');
                setSubmitStatus('');
            } catch (error) {
                console.error('Ошибка загрузки вопроса:', error);
            }
        };
        loadQuestion();
    }, [testId, currentQues]);

    const handleAnswerSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post(
                `http://localhost:8000/api/questions/${testId}/${currentQues}/`,
                { answer_text: selectedAnswer }
            );
            setSubmitStatus('Ответ успешно сохранен!');
            setTimeout(() => setSubmitStatus(''), 3000);
        } catch (error) {
            console.error('Ошибка сохранения ответа:', error);
            setSubmitStatus('Ошибка сохранения ответа!');
        }
    };

    if (!questionData) return <div>Загрузка вопроса...</div>;

    return (
        <div className="test-interface">
            <div className="question-progress">
                Вопрос {currentQues} из {questionData.navigation.total}
            </div>

            <form onSubmit={handleAnswerSubmit}>
                <div className="question-card">
                    <h3>{questionData.question.question_text}</h3>

                    <div className="answer-options">
                        {questionData.options.map(option => (
                            <label key={option.id_answ} className="option-label">
                                <input
                                    type="radio"
                                    name="answer"
                                    value={option.answer_text}
                                    checked={selectedAnswer === option.answer_text}
                                    onChange={(e) => setSelectedAnswer(e.target.value)}
                                />
                                <span className="option-text">{option.answer_text}</span>
                            </label>
                        ))}
                    </div>
                </div>

                <div className="navigation-controls">
                    <button
                        type="button"
                        className="nav-button"
                        disabled={!questionData.navigation.previous}
                        onClick={() => setCurrentQues(prev => prev - 1)}
                    >
                        Назад
                    </button>

                    <button type="submit" className="submit-button">
                        Сохранить ответ
                    </button>

                    <button
                        type="button"
                        className="nav-button"
                        disabled={!questionData.navigation.next}
                        onClick={() => setCurrentQues(prev => prev + 1)}
                    >
                        Далее
                    </button>
                </div>

                {submitStatus && (
                    <div className={`status-message ${submitStatus.includes('успешно') ? 'success' : 'error'}`}>
                        {submitStatus}
                    </div>
                )}
            </form>
        </div>
    );
};

export default TestInterface;
