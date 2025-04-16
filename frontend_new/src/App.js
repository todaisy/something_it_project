import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TestInterface from './TestInterface';
import { useParams } from 'react-router-dom';

function App() {
    const { testId } = useParams(); // Получаем testId из URL
    const [sessionId, setSessionId] = useState(localStorage.getItem('test_session') || null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const initializeSession = async () => {
            try {
                if (!sessionId) {
                    // Создаем новую сессию
                    const response = await axios.post('http://127.0.0.1:8000/api/start-session/');
                    const newSessionId = response.data.session_id;

                    localStorage.setItem('test_session', newSessionId);
                    setSessionId(newSessionId);
                }
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        initializeSession();
    }, [sessionId]);

    if (loading) {
        return <div>Инициализация теста...</div>;
    }

    if (error) {
        return (
            <div className="error">
                <h2>Ошибка инициализации</h2>
                <p>{error}</p>
                <button onClick={() => window.location.reload()}>Повторить</button>
            </div>
        );
    }

    return (
        <div className="App">
            <h1>Система тестирования</h1>
            {/* Передаем оба пропса: */}
            <TestInterface
                sessionId={sessionId}
                testId={testId}
            />
        </div>
    );
}

export default App;