import './App.css';
import createClass from 'create-react-class';
import React from 'react';
import { Button } from 'react-bootstrap';
import { ButtonToolbar } from 'react-bootstrap';
//import { Button } from 'reactstrap';
import Particles from 'react-particles-js';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/custom.css';

var HomePage = createClass ({

    getInitialState: function (){
                        return {text: 'Welcome'}
                                },




    render: function () {

        return (
                <div className = 'Home'>


                            <h1 className = 'titolo-home' id='prova'> Sistema di monitoraggio social per la PA </h1>


                            <Particles


                                       params={{
                                                    particles: {
                                                        number: {value: 100},
                                                        color: {value: '#cf2c2c'},

                                                    },
                                                    interactivity: {onhover: {enable: true, mode: 'repulse'}}
                                                }}


                                      style={{
                                        position: 'absolute',
                                        zIndex: 0,
                                        height: '250%',
                                        width: '100%'

                                      }}



                            />
                        <br />

                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <div className='prova-canvas'>
                            <h2 className='title-over-plot'> Scegli se effettuare l'analisi tramite hashtag o topic</h2>
                            <p className='title-over-plot'> Helo</p>

                            <div className='tableButton'>
                            <form action="/api_dati_tweet" method="get">
                                <button type="submit" className="btn btn-outline-secondary" onClick={this.props.scegliAnalisi}>Hashtag</button>
                                <button type="submit" className="btn btn-outline-secondary" onClick={this.props.scegliAnalisi}>Topic</button>
                            </form>
                            </div>


                        </div>

                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <div className='canvas-due'>
                            <h2 className='title-over-plot'> Scopri di più sul progetto </h2>
                            <div className='tableButton'>
                                <p className='title-over-plot'> Helo</p>
                                <a  className="btn btn-outline-secondary"  href='#chi-siamo' role="button">Chi siamo</a>
                                <a  href='#progetto' className="btn btn-outline-secondary"  role="button">Progetto</a>
                                <a  className="btn btn-outline-secondary" href='#contribuisci' role="button">Contribuisci</a>

                            </div>
                        </div>
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />

                        <br />
                        <br />
                        <div className='canvas-progetto-2'>
                            <h2 className='title-over-plot' id='progetto'> Chi siamo </h2>
                            <p>
                            Scrivi Scrivi  Scrivi  Scrivi  Scrivi  Scrivi  Scrivi
                            Scrivi  Scrivi  Scrivi  Scrivi  Scrivi  Scrivi Scrivi
                            Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi
                            Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi
                            Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi
                            </p>
                        </div>
                        <br />
                        <br />
                        <br />
                        <br />
                        <Particles


                                       params={{
                                                    particles: {
                                                        number: {value: 100},
                                                        color: {value: '#cf2c2c'},

                                                    },
                                                    interactivity: {onhover: {enable: true, mode: 'repulse'}}
                                                }}


                                      style={{
                                        position: 'absolute',
                                        zIndex: 0,
                                        height: '250%',
                                        width: '100%'

                                      }}



                            />
                        <br />
                        <br />
                        <br />
                        <div className='canvas-progetto'>
                            <h2 className='title-over-plot' id='progetto'> Progetto </h2>
                            <p>
                            Scrivi Scrivi  Scrivi  Scrivi  Scrivi  Scrivi  Scrivi
                            Scrivi  Scrivi  Scrivi  Scrivi  Scrivi  Scrivi Scrivi
                            Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi
                            Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi
                            Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi
                            </p>
                        </div>
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <div className='canvas-contribuisci'>
                            <h2 className='title-over-plot' id='contribuisci'> Contribuisci </h2>
                            <p>
                            Scrivi Scrivi  Scrivi  Scrivi  Scrivi  Scrivi  Scrivi
                            Scrivi  Scrivi  Scrivi  Scrivi  Scrivi  Scrivi Scrivi
                            Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi
                            Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi
                            Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi Scrivi
                            </p>
                        </div>
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <Particles


                                       params={{
                                                    particles: {
                                                        number: {value: 100},
                                                        color: {value: '#cf2c2c'},

                                                    },
                                                    interactivity: {onhover: {enable: true, mode: 'repulse'}}
                                                }}


                                      style={{
                                        position: 'absolute',
                                        zIndex: 0,
                                        height: '100%',
                                        width: '100%'

                                      }}



                            />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />






                </div>
                )

                        }




                            });




export default HomePage;