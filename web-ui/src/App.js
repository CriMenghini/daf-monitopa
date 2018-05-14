import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import createClass from 'create-react-class';
import BoardHashtag from './Board';
import Hashtag  from './Hashtag';
import SearchBar from './SearchBar';
import Menu from './Menu';
import { Container, Row, Col } from 'reactstrap';
import VisualisationGrid from './GridVisualisation';
import TopUsers from './ParallelBrushAxes';




var App = createClass({
  render() {
    return (

      <div className='App'>
         <div className="Teal">
              <div className='Title'>
                <h1>PA in ascolto</h1>
              </div>
         </div>
         <div className='Sidebar' id='mySidebar'>
              <div className='Sidebar-hashtag'>
                <SearchBar />
                <br/>
              </div>


         </div>
         <div className='Visualisation'>
            <div>
            <h4>Questo hashtag compare nei seguenti topic</h4>

            </div>

            <br/>
            <VisualisationGrid />
            <br/>
            <br/>
            <br/>
            <h1>
                In che consiste il progetto?
            </h1>
            <p>
                Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you?
                Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you?
                Hello, how are you? Hello, how are you? Hello, how are you? Hello, how are you?
            </p>
         </div>





      </div>
    );
  }
});

export default App;


