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
import ChooseTopic from './TopicButton';
import '../node_modules/bootstrap-italia/dist/css/bootstrap-italia.min.css';
import '../node_modules/bootstrap-italia/dist/css/italia-icon-font.css';


var App = createClass({
  render() {
    return (

      <div className='App'>
              <div className='Title'>
                <h1 class='title-name'>T(wi)scany</h1>
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
                <ChooseTopic />
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



