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
        <button class="button-82-pushable" role="button" onClick={() => setLabel((btnLabel) => btnLabel == 'Submit' ? 'Submitted!' : 'Submit')}>
          <span class="button-82-shadow"></span>
          <span class="button-82-edge"></span>
          <span class="button-82-front text">
            {btnLabel}
          </span>
        </button>
      </div>
    </>
  );
}

export default App