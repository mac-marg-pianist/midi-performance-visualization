import React, { Component } from 'react';
import './styles/main.scss'
import NoteSequence from './notes/NoteSequence'
import Scroll from './Scroll'
import Controller from './control_ex'
import Columns from 'react-columns'
import performJson from './json/Ali01_spr.json'
import scoreJson from './json/midi_cleaned_spr.json'

class App extends Component {
  state = {
    perform_notes: performJson.notes,
    score_notes: scoreJson.notes,
    total_time: 100,
    current_time: 0,
    play: true
  };


  setTime = (ratio) => {
    const { total_time } = this.state;
    this.setState({
      current_time: total_time * ratio
    })
  };

  render() {
    const { current_time, play } = this.state;
    return (
      <div className="App">
        <header className='App-head'>
          Performance Analyzer v0.1
        </header>
        <div className="App-body">
          <Scroll
            setTime = {this.setTime}
            time = {current_time}
            play = {play}
          />
          <div>
            current_time = {current_time}
          </div>
          <div className="App-display">
            roll1
          </div>
          <div className="App-control">
            <Controller/>
          </div>

          
        </div>

      </div>
    );
  }
}

export default App;
