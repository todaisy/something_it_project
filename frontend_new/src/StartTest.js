import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const StartTest = () => {
  const navigate = useNavigate();
  const [error, setError] = useState('');

  const handleStartTest = async () => {
    try {
      setError(''); // Сбросить ошибку перед запросом
      const response = await axios.post('http://localhost:8000/api/start-session/');

      // Проверка ответа сервера
      if (!response.data?.session_id || !response.data?.test_id) {
        throw new Error('Неверный формат ответа сервера');
      }

      localStorage.setItem('test_session', response.data.session_id);
      navigate(`/test/${response.data.test_id}`); // Используйте test_id из ответа

    } catch (error) {
      setError('Не удалось начать тест. Проверьте консоль для деталей.');
      console.error('Ошибка создания сессии:', error.response?.data || error.message);
    }
  };

  return (
    <div>
      <button onClick={handleStartTest}>Начать тест</button>
      {error && <div style={{ color: 'red', marginTop: '10px' }}>{error}</div>}
    </div>
  );
};

export default StartTest;