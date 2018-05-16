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
import numTweet from './data/numberTweet_hashtag.js';
import Retweet from './data/TopRetweet.js';



import Viz from './tryViz';
import Search from './trySearch';

const API = 'http://127.0.0.1:5000/api_dati_tweet';


var App =  createClass({


          getInitialState: function (){
                        return {sentence: 'inserire qui hashtag', numtweet: numTweet, numretweet: Retweet[0].x}
                    },




        handleSubmit: function(event) {
                            event.preventDefault();

                            fetch('http://127.0.0.1:5000/api_dati_tweet', {method: 'post',
                                        headers: {'Content-Type':'application/json'},
                                        body: JSON.stringify({"selectedHashtag": this.state.sentence})})

                                        .then(response => {
                                          return response.json();}
                                        )
                                        .then(data => this.setState({numtweet: data.numTweet,  numretweet: data.NumRetweet, percent: data.numTweet}))
                                        },

        handleClick: function (event){
                            this.setState({sentence: event.target.value, percent: this.state.numtweet})
                                      },

        render() {

            return (<div className='App'>
                        <div className='Title'>
                          <h1 className='title-name'>T(wi)scany</h1>
                        </div>

                       <div className='Sidebar' id='mySidebar'>
                            <div className='Sidebar-hashtag'>
                              <SearchBar { ...this.props } { ...this.state} funzioneSubmit={this.handleSubmit} funzioneClick={this.handleClick}/>
                              <br/>
                            </div>
                       </div>

                       <div className='Visualisation'>
                             <div>
                                  <h4>Questo hashtag compare nei seguenti topic</h4>
                                  <ChooseTopic />
                             </div>
                                <br/>
                                <VisualisationGrid { ...this.props } { ...this.state} funzioneSubmit={this.handleSubmit} funzioneClick={this.handleClick}/>
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

                    </div>     ) }




                                });

export default App;





