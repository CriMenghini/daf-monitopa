import React, { Component } from 'react';
import createClass from 'create-react-class';
import './App.css';
import listaHash from './data/listaHash.js';
import BoardTopic  from './BoardTopic';

var ChooseTopic = createClass({


    getInitialState: function (){
        return {items: listaHash.slice(0,5)}
                },

    render: function (){
        return (<div className='TopicContainer'>
                    <h3 className='Topic'>Choose</h3>
                    <BoardTopic  { ...this.props } { ...this.state} />
                </div>)
    }
});


export default ChooseTopic;