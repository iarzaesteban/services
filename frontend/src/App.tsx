import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { REACT_APP_API_URL } from './constants';

function App() {
  const [backendMessage, setBackendMessage] = useState<string>('');

  useEffect(() => {
    fetch(`${REACT_APP_API_URL}/api/health/`)
      .then(response => response.json())
      .then(data => setBackendMessage(data.status))
      .catch(error => console.error('Error connecting to backend:', error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {backendMessage ? `Backend says123: ${backendMessage}` : 'Connecting to backend...'}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
