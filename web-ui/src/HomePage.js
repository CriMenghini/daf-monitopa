import './App.css';
import createClass from 'create-react-class';
import React from 'react';
import { Button } from 'react-bootstrap';
import { ButtonToolbar } from 'react-bootstrap';
//import { Button } from 'reactstrap';
import Particles from 'react-particles-js';
import 'bootstrap/dist/css/bootstrap.min.css';
//import 'bootstrap/dist/css/custom.css';
import './css/fontawesome-all.css';

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
                            <h3 className='title-over-plot'> Scegli se effettuare l'analisi tramite hashtag o topic</h3>
                            <p className='title-over-plot' style={{fontSize:'14px'}}>

                            </p>

                            <div className='tableButton'>
                            <form action="/api_dati_tweet" method="get">
                                <button type="submit" className="bottone mx-2"  onClick={this.props.scegliAnalisiHash}>Hashtag</button>
                                <button type="submit" className="bottone mx-2" onClick={this.props.scegliAnalisiTopic}>Topic</button>
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
                            <h3 className='title-over-plot'> Scopri di più sul progetto </h3>
                            <p className='title-over-plot'> </p>
                            <div className='tableButton'>
                                <a  className="bottone"  href='#chi-siamo' role="button">Chi siamo</a>
                                <a  href='#progetto' className="bottone mx-2"  role="button">Progetto</a>
                                <a  className="bottone" href='#contribuisci' role="button">Contribuisci</a>


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
                            <h3 className='title-over-plot' id='chi-siamo'> Chi siamo </h3>
                            <p className='paragraphs'>
                                Il progetto è stato sviluppato dal <a href="https://teamdigitale.governo.it/it/47-content.htm">Team per
                                la Trasformazione Digitale</a> della Presidenza del Consiglio dei Ministri.
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
                            <h3 className='title-over-plot' id='progetto'> Progetto </h3>
                            <p className='paragraphs'>
                                Ogni minuto, l’intera popolazione mondiale pubblica circa 452 mila post su Twitter. La domanda che ci poniamo è:
                                può la Pubblica Amministrazione utilizzare la mole di tweet che i cittadini creano? Se si, in che modo?

                                Per continuare a leggere sul progetto clicca <a href="https://dataportal-private.daf.teamdigitale.it/#/userstory/list/6095a70d-61f8-4618-a42f-c9ccf1fd02f1">qui</a>.
                            </p>
                        </div>
                        <br />
                        <br />
                        <br/>

                        <br />
                        <br />
                        <br />
                        <br />
                        <div className='canvas-contribuisci'>
                            <h3 className='title-over-plot' id='contribuisci'> Contribuisci </h3>
                            <p className='paragraphs'>
                                Il codice utilizzato per costruire l'applicazione è contenuto per intero della
                                repository di Github cui questo sito punta. In accordo con lo spirito del Team,
                                invitiamo qualsiasi appassionato a contribuire per il mantenimento ed il
                                miglioramento di questo prototipo con l'obiettivo di renderlo disponibile per
                                la Pubblica Amministrazione.
                                <br/>
                                <br/>
                                <br/>
                                <a href='#'><i class="fab fa-github fa-lg size:7x"></i></a>
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
