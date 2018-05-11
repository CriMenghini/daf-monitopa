import React, { Component } from 'react';
import './App.css';
import { Container, Row, Col } from 'reactstrap';
import createClass from 'create-react-class';
import NumberSquare from './NumberSquare';
import TopUsers from './ParallelBrushAxes';
import { _ } from "jquery";
var Ajv = require('ajv');

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
                                     <NumberSquare />
                                </div>
                          </Col>
                          <Col md="4" className="col-3">
                                <div>
                                     Come va
                                     <NumberSquare />
                                </div>
                          </Col>
                        </Row>
                        <Row className="prova">
                            <TopUsers />
                        </Row>
                    </Container>
                </div>)
    },
});



export default VisualisationGrid;