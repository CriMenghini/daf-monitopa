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
              </div>

              <div className='Sidebar-topic'>
                <h2>Here we place the topic viz</h2>
              </div>
         </div>
         <div className='Visualisation'>
            <h4>CIAONE</h4>


            <br/>
            <VisualisationGrid />
         </div>


      </div>
    );
  }
});

export default App;


