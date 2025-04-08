import { useEffect, useState } from "react";


function App() {
  return (
    function App() {
      const [data, setData] = useState(null);
      useEffect(() => {
        fetch('http://localhost:8000/api/hello/')
          .then(response => response.json())
          .then(data => setData(data.message));
      }, []);
    
      return (
        <div>
          <h1>Данные из Django:</h1>
          <p>{data || 'Загрузка...'}</p>
        </div>
      );
    }
  );
}

export default App;
