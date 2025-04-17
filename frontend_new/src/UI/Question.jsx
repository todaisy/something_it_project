import React from "react";

const Question = ({ question }) => {
  return (
    <div className="question-item">
      <h2>{question.title}</h2>
      
    </div>
  );
};

export default Question;