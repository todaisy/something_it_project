import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TestInterface = ({ testId }) => {
    const [currentQues, setCurrentQues] = useState(1);
    const [questionData, setQuestionData] = useState(null);
    const [selectedAnswer, setSelectedAnswer] = useState('');

    useEffect(() => {
        const loadQuestion = async () => {
            try {
                const response = await axios.get(`/api/questions/${testId}/${currentQues}/`);
                setQuestionData(response.data);
                setSelectedAnswer(response.data.current_answer);
            } catch (error) {
                console.error('Error loading question:', error);
            }
        };
        loadQuestion();
    }, [testId, currentQues]);

    const handleAnswerSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post(`/api/questions/${testId}/${currentQues}/`, {
                answer_text: selectedAnswer
            });
            alert('Ответ успешно сохранен!');
        } catch (error) {
            console.error('Error saving answer:', error);
        }
    };

    if (!questionData) return <div>Загрузка...</div>;

    return (
        <div className="test-container">
            <h2>Вопрос {currentQues} из {questionData.navigation.total}</h2>
            <div className="question-text">
                {questionData.question.question_text}
            </div>

            <form onSubmit={handleAnswerSubmit}>
                <div className="answer-options">
                    {questionData.options.map(option => (
                        <label key={option.id_answ} className="option-item">
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

                <div className="navigation-buttons">
                    {questionData.navigation.previous && (
                        <button
                            type="button"
                            className="nav-btn prev-btn"
                            onClick={() => setCurrentQues(prev => prev - 1)}
                        >
                            ← Предыдущий
                        </button>
                    )}

                    <button type="submit" className="save-btn">
                        Сохранить ответ
                    </button>

                    {questionData.navigation.next && (
                        <button
                            type="button"
                            className="nav-btn next-btn"
                            onClick={() => setCurrentQues(prev => prev + 1)}
                        >
                            Следующий →
                        </button>
                    )}
                </div>
            </form>
        </div>
    );
};

export default TestInterface;


/*
import React, { useState, useEffect } from "react";
import Question from "./Question";

const Questions = () => {
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        const response = await fetch("http://localhost:8000/");
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        setQuestions(data);
      } catch (err) {
        setError(err.message || "Error fetching questions");
      } finally {
        setLoading(false);
      }
    };
  
    fetchQuestions();
  }, []);

  if (loading) {
    return <div className="loading">Loading questions...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="questions-list">
      {questions.length > 0 ? (
        questions.map((question) => (
          <Question key={question.id} question={question} />
        ))
      ) : (
        <div className="no-questions">No questions found</div>
      )}
    </div>
  );
};

export default Questions;
*/
