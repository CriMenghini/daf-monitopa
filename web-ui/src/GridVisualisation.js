import React, { Component } from 'react';
import './App.css';
import { Container, Row, Col } from 'reactstrap';
import createClass from 'create-react-class';
import TopUsers from './TopUsers';
import { _ } from "jquery";
import NumTweet from './NumberTweet';
import Sentiment from './TweetSentiment';
import NumRetweet from './NumberRetweet';
import UtentiUnici from './UtentiUnici';
import TimeSeries from './TimeSeries';
import numTweet from './data/numberTweet_hashtag.js';
import Retweet from './data/TopRetweet.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Collapse, Button, CardBody, Card } from 'reactstrap';
//import {} from 'save-svg-as-png/lib/saveSvgAsPng.js';
//var saveSvgAsPng = require('./saveSvgAsPng');




var VisualisationGrid = createClass({

    getInitialState: function (){
                        return {collapse1: false, collapse2: false,
                                collapse3: false, collapse4: false,
                                collapse5: false, collapse6: false}
                                },

    toggle1: function() {
    this.setState({ collapse1: !this.state.collapse1 });
    },

    toggle2: function() {
    this.setState({ collapse2: !this.state.collapse2 });
    },

    toggle3: function() {
    this.setState({ collapse3: !this.state.collapse3 });
    },

    toggle4: function() {
    this.setState({ collapse4: !this.state.collapse4 });
    },

    toggle5: function() {
    this.setState({ collapse5: !this.state.collapse5 });
    },

    toggle6: function() {
    this.setState({ collapse6: !this.state.collapse6 });
    },

    handleDownload: function(){
            //saveSvgAsPng.saveSvgAsPng(document.getElementById("svgprova"), "diagram.png");
            },

    render: function (){
        return (<div>
                    <Container className='GridViz'>
                        <Row>
                          <Col md="4" className="col-1">
                                <div className="NumTweet">
                                    Numero di Tweet
                                    <NumTweet { ...this.props } { ...this.state} funzioneSubmit={this.props.funzioneSubmit} funzioneClick={this.props.funzioneClick}/>

                                    <button onClick={this.handleDownload}></button>

                                    <div>
                                    <Button color="secondary" onClick={this.toggle1} style={{ marginTop:'0px',marginBottom: '1rem' }}>Toggle</Button>
                                    <Collapse isOpen={this.state.collapse1}>
                                      <Card>
                                        <CardBody style={{position: 'absolute', zIndex:10, backgroundColor:'grey', color:'white'}}>
                                            Questo grafico definisce il numero di Tweet scritti, escludendo i retweet, che contengono
                                            l'hashtag selezionato.
                                        </CardBody>
                                      </Card>
                                    </Collapse>
                                    </div>

                                </div>

                          </Col>
                          <Col md="4" className="col-2">
                                <div className="NumRetweet">
                                     Top 10 Retweet
                                     <NumRetweet dati={Retweet} { ...this.props } { ...this.state} funzioneSubmit={this.props.funzioneSubmit} funzioneClick={this.props.funzioneClick}/>

                                    <div>
                                    <Button color="secondary" onClick={this.toggle2} style={{ marginTop:'0px', marginBottom: '1rem'}}>Toggle</Button>
                                    <Collapse isOpen={this.state.collapse2}>
                                      <Card>
                                        <CardBody style={{position: 'absolute', zIndex:10, backgroundColor:'grey', color:'white'}}>
                                            Questo grafico definisce il numero di Tweet scritti, escludendo i retweet, che contengono
                                            l'hashtag selezionato.
                                        </CardBody>
                                      </Card>
                                    </Collapse>
                                    </div>

                                </div>
                          </Col>
                          <Col md="4" className="col-3">
                                <div className="TweetSentiment">
                                     Tweet Sentiment
                                     <br/>
                                     <Sentiment { ...this.props } { ...this.state} funzioneSubmit={this.props.funzioneSubmit} funzioneClick={this.props.funzioneClick} />

                                    <div>
                                    <Button color="secondary" onClick={this.toggle3} style={{ marginBottom: '1rem' }}>Toggle</Button>
                                    <Collapse isOpen={this.state.collapse3}>
                                      <Card>
                                        <CardBody style={{position: 'absolute', zIndex:10, backgroundColor:'grey', color:'white'}}>
                                            Questo grafico definisce il numero di Tweet scritti, escludendo i retweet, che contengono
                                            l'hashtag selezionato.
                                        </CardBody>
                                      </Card>
                                    </Collapse>
                                    </div>


                                </div>
                          </Col>
                        </Row>

                        <Row>
                          <Col md="4" className="col-1">
                                <div className="UserUnique">
                                    Utenti unici nel tempo
                                     <UtentiUnici { ...this.props } { ...this.state} />

                                    <div>
                                    <Button color="secondary" onClick={this.toggle4} style={{ marginBottom: '1rem' }}>Toggle</Button>
                                    <Collapse isOpen={this.state.collapse4}>
                                      <Card>
                                        <CardBody style={{position: 'absolute', zIndex:10, backgroundColor:'grey', color:'white'}}>
                                            Questo grafico definisce il numero di Tweet scritti, escludendo i retweet, che contengono
                                            l'hashtag selezionato.
                                        </CardBody>
                                      </Card>
                                    </Collapse>
                                    </div>
                                </div>
                          </Col>
                          <Col md="4" className="col-2">
                                <div className="TopUsers">
                                     Top 10 co-hashtag
                                    <TopUsers { ...this.props } { ...this.state} />

                                    <div>
                                    <Button color="secondary" onClick={this.toggle5} style={{ marginBottom: '1rem' }}>Toggle</Button>
                                    <Collapse isOpen={this.state.collapse5}>
                                      <Card>
                                        <CardBody style={{position: 'absolute', zIndex:10, backgroundColor:'grey', color:'white'}}>
                                            Questo grafico definisce il numero di Tweet scritti, escludendo i retweet, che contengono
                                            l'hashtag selezionato.
                                        </CardBody>
                                      </Card>
                                    </Collapse>
                                    </div>
                                </div>
                          </Col>
                          <Col md="4" className="col-3">
                                <div className="StreamTweet">
                                     Tweet stream
                                     <TimeSeries { ...this.props } { ...this.state} />

                                     <div>
                                    <Button color="secondary" onClick={this.toggle6} style={{ marginBottom: '1rem' }}>Toggle</Button>
                                    <Collapse isOpen={this.state.collapse6}>
                                      <Card>
                                        <CardBody style={{position: 'absolute', zIndex:10, backgroundColor:'grey', color:'white'}}>
                                            Questo grafico definisce il numero di Tweet scritti, escludendo i retweet, che contengono
                                            l'hashtag selezionato.
                                        </CardBody>
                                      </Card>
                                    </Collapse>
                                    </div>
                                </div>



                          </Col>
                        </Row>
                    </Container>






                </div>)
    },
});



export default VisualisationGrid;