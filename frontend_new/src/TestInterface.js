import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';

const TestInterfaceComponent = () => {
  const { testId } = useParams();
  const [currentQues, setCurrentQues] = useState(1);
  const [questionData, setQuestionData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const sessionId = localStorage.getItem('test_session');
  const navigate = useNavigate();
  const abortControllerRef = useRef(new AbortController());

  useEffect(() => {
    const fetchData = async () => {
      if (!sessionId) {
        navigate('/');
        return;
      }

      abortControllerRef.current.abort(); // Отменяем предыдущий запрос
      abortControllerRef.current = new AbortController();

      try {
        setIsLoading(true);
        setError(null);

        const response = await axios.get(
          `http://localhost:8000/api/question/${sessionId}/${testId}/${currentQues}/`,
          { signal: abortControllerRef.current.signal }
        );

        if (response.data.navigation.next === null && currentQues === response.data.navigation.total) {
          navigate('/results');
        }

        setQuestionData(response.data);
      } catch (err) {
        if (!axios.isCancel(err)) {
          console.error('Ошибка загрузки:', err);
          setError('Не удалось загрузить вопрос');
          navigate('/');
        }
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();

    return () => abortControllerRef.current.abort();
  }, [currentQues, testId, sessionId, navigate]);

  const handleNext = () => {
    setCurrentQues(prev => Math.min(prev + 1, questionData?.navigation?.total || 1));
  };

  const handlePrev = () => {
    setCurrentQues(prev => Math.max(prev - 1, 1));
  };

  if (!sessionId) return <div>Перенаправление...</div>;
  if (error) return <div>{error}</div>;
  if (isLoading) return <div>Загрузка...</div>;

  return (
    <div>
      <h2>Вопрос {currentQues} из {questionData.navigation.total}</h2>
      <h3>{questionData.question.text}</h3>
      <ul>
        {questionData.options.map(option => (
          <li key={option.id_answ}>{option.text}</li>
        ))}
      </ul>
      <div>
        <button
          onClick={handlePrev}
          disabled={currentQues === 1}
        >
          Назад
        </button>
        <button
          onClick={handleNext}
          disabled={currentQues === questionData.navigation.total}
        >
          Далее
        </button>
      </div>
    </div>
  );
};

export default TestInterfaceComponent;