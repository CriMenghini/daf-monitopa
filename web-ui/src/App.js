import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import createClass from 'create-react-class';
import BoardHashtag from './Board';
import Hashtag  from './Hashtag';
import SearchBar from './SearchBar';
import { Container, Row, Col } from 'reactstrap';
import VisualisationGrid from './GridVisualisation';
import TopUsers from './TopUsers';
import ChooseTopic from './ChooseTopic';
import numTweet from './data/numberTweet_hashtag.js';
import Retweet from './data/TopRetweet.js';
import SentimentTweet from './data/sentimentData.js';
import UniqueUser from './data/uniqueUser.js';
import posTweet from './data/positiveTweet.js';
import negTweet from './data/negativeTweet.js';
import neuTweet from './data/neutralTweet.js';
import listaHash from './data/listaHash.js';
import {Collapse} from 'react-collapse';
import 'bootstrap/dist/css/bootstrap.min.css';
//import 'bootstrap/dist/css/custom.css';
import Particles from 'react-particles-js';
//import 'saveSvgAsPng.js';
var _ = require('lodash');



const API = 'http://127.0.0.1:5000/hashtag_api';


var App =  createClass({


          getInitialState: function (){
                        return {sentence: "Seleziona l'hashtag da analizzare",

                                hashtags: listaHash,
                                numtweet: numTweet,
                                numretweet: Retweet,
                                sentiment: SentimentTweet,
                                unique: UniqueUser,
                                streampos: posTweet,
                                streamneg: negTweet,
                                //streamneu: neuTweet,
                                DataSet:[{'x': 1, 'y': 100, 'label': '#ciao'}, {'x': 2, 'y': 108, 'label': "#hello"}, {'x': 3, 'y': 50, 'label': '#howareyou'}, {'x': 4, 'y': 23, 'label': '#renzi'}, {'x': 5, 'y': 22, 'label': '#pa'}, {'x': 6, 'y': 4, 'label': '#ca'}, {'x': 7, 'y': 3, 'label': '#oioio'}, {'x': 8, 'y': 2, 'label': '#hotmail'}, {'x': 9, 'y': 2, 'label': '#popopo'}, {'x': 10, 'y': 2, 'label': "#casa"}]
              }},



        handleSubmit: function(event) {
                            event.preventDefault();

                            fetch(API, {method: 'post',
                                        headers: {'Content-Type':'application/json'},
                                        body: JSON.stringify({"selectedHashtag": this.state.sentence})})

                                        .then(response => {
                                          return response.json();}
                                        )
                                        .then(data => this.setState({numtweet: data.numTweet,
                                                                     numretweet: data.NumRetweet,
                                                                     percent: data.numTweet,
                                                                     sentiment: data.Sentiment,
                                                                     unique: data.Unique,
                                                                     streampos: data.StreamPos,
                                                                     streamneg: data.StreamNeg,
                                                                     streamneu: data.StreamNeu,
                                                                     DataSet: data.dataSet}))
                                        },

        handleClick: function (event){
                            this.setState({sentence: event.target.value,
                                           percent: this.state.numtweet})
                                      },

        render() {

            return (<div className='App'>
                        <div className='Title'>
                          <Particles


                                       params={{
                                                    particles: {
                                                        number: {value: 80},
                                                        color: {value: '#cf2c2c'},

                                                    },
                                                    interactivity: {onhover: {enable: true, mode: 'repulse'}}
                                                }}


                                      style={{
                                        position: 'absolute',
                                        zIndex: 0


                                      }}



                            />

                                <div className="row mx-3 my-4">
                                  <a href='/'><i className="fa fa-home fa-lg text-white icona-home"/></a>
                                  <h1 className="title-hashtag ml-4">#{this.state.sentence}</h1>
                                </div>


                        </div>


                       <div className='Sidebar' id='mySidebar'>
                            <div className='Sidebar-hashtag'>
                              <SearchBar { ...this.props } { ...this.state} funzioneSubmit={this.handleSubmit} funzioneClick={this.handleClick}/>
                              <br/>
                            </div>
                       </div>

                       <div className='Visualisation'>

                                <VisualisationGrid { ...this.props } { ...this.state} funzioneSubmit={this.handleSubmit} funzioneClick={this.handleClick}/>
                       </div>

                    </div>     ) }




                                });

export default App;





