import React, { Component } from 'react';
import './App.css';
import { Container, Row, Col } from 'reactstrap';
import createClass from 'create-react-class';
import NumberSquare from './NumberSquare';

var VisualisationGrid = createClass({
    render: function (){
        return (<div>
                    <Container className='GridViz'>
                        <Row>
                          <Col md="4" className="col-1">
                                <div className="NumTweet">
                                    Come va
                                    <NumberSquare />
                                </div>
                          </Col>
                          <Col md="4" className="col-2">
                                <div>
                                    Come va
                                </div>
                          </Col>
                          <Col md="4" className="col-3">
                                <div>
                                    Come va
                                </div>
                          </Col>
                        </Row>
                    </Container>
                </div>)
    },
});



export default VisualisationGrid;