import React, { Component } from 'react';
import createClass from 'create-react-class';
import Topic  from './TopicButton';
import './App.css';
import listaHash from './data/listaHash.js';

var BoardTopic = createClass({



    eachHashtag: function (text, i){
        return (<Topic key={i} index={i} { ...this.props } { ...this.state} >
                    {text}
                </Topic>
           );

    },

    render: function (){
        return (<div className='boardTopic'>
                    {this.props.items.map(this.eachHashtag)}
                </div>)
    }
});

export default BoardTopic;