import { useState } from 'react'
import './App.css'
import React from 'react';

function App() {
  const [btnLabel, setLabel] = useState('Submit')

  return (
    <>
      <div className="App">
      <h1 className='App-header'>Plagiarism Check</h1>
      <p>Enter Text to check for originality</p>
      <form>
        <textarea />
      </form>
        <button className="button-82-pushable" role="button" onClick={() => setLabel((btnLabel) => btnLabel == 'Submit' ? 'Submitted!' : 'Submit')}>
          <span className="button-82-shadow"></span>
          <span className="button-82-edge"></span>
          <span className="button-82-front text">
            {btnLabel}
          </span>
        </button>
      </div>
    </>
  );
}

export default App