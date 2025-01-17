import { useState } from 'react'
import './App.css'
import React from 'react';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="App">
      <h1 className='App-header'>Plagiarism Check</h1>
      <p>Enter Text to check for originality</p>
      <form>
        <label className='inputLabel'></label>
        <textarea />
      </form>
      </div>
    </>
  );
}

export default App