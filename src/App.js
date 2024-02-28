import React from 'react';
import './App.css';
import Map from './Map';
import Buttons from './Buttons';
import PrintNotes from './PrintNotes';

function App() {
  return (
    <div className="App">
      <div className="App-header">
            <Map />
      </div>
      <div className='Rightside'>
      <div className='Notes'>
        <PrintNotes />
      </div>
      <div className='Buttons'>
          <Buttons />
      </div>
      </div>
    </div>
  );
}

export default App;
