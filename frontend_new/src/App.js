import React, { useState, useEffect } from 'react'; // Добавьте хуки
import axios from 'axios'; // Импортируйте axios
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate
} from 'react-router-dom';
import TestInterfaceComponent from './TestInterface';
import StartTest from './StartTest';

function App() {
  return (
    <Router>
      <div className="App">
        <h1>Система тестирования</h1>
        <Routes>
          <Route path="/" element={<StartTest />} />
          <Route
            path="/test/:testId"
            element={<ProtectedRoute><TestInterfaceComponent /></ProtectedRoute>}
          />
        </Routes>
      </div>
    </Router>
  );
}

// Компонент для проверки сессии
const ProtectedRoute = ({ children }) => {
  const [isValidSession, setIsValidSession] = useState(null); // Теперь useState определен
  const sessionId = localStorage.getItem('test_session');

  useEffect(() => { // Теперь useEffect определен
    const verifySession = async () => {
      try {
        await axios.get(`http://localhost:8000/api/verify-session/${sessionId}/`);
        setIsValidSession(true);
      } catch (error) {
        localStorage.removeItem('test_session');
        setIsValidSession(false);
      }
    };

    if (sessionId) verifySession();
    else setIsValidSession(false);
  }, []);

  if (isValidSession === null) return <div>Проверка сессии...</div>;
  return isValidSession ? children : <Navigate to="/" replace />;
};

export default App;



/* <Route path="/contact" element={<Contact />} />
 <Route path="/" element={<Home />} />
 <Route path="/results" element={<Results />} />
*/