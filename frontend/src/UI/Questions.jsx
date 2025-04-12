import React, { useState, useEffect } from "react";
import axios from "axios";
import Question from "./Question";

const Questions = () => {
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        const response = await axios.get("http://localhost:8000/");
        setQuestions(response.data);
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