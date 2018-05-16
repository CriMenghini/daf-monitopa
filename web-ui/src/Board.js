import React, { Component } from 'react';
import createClass from 'create-react-class';
import Comment from './Comment';
import Hashtag  from './Hashtag';
import './App.css';


var BoardHashtag = createClass({

    getInitialState: function (){
        return {items: this.props.inheritState}
    },

    componentWillReceiveProps: function(nextProps){
	if(nextProps.inheritState){
		this.setState({
			items: nextProps.inheritState
		})
	}
},

    eachHashtag: function (text, i){
        return (<Hashtag key={i} index={i}  { ...this.props } { ...this.state} funzioneSubmit={this.props.funzioneSubmit} funzioneClick={this.props.funzioneClick}>
                    {text}
                </Hashtag>
           );

    },

    render: function (){
        return (<div className='boardHash'>
                    {this.state.items.map(this.eachHashtag)}
                </div>)
    }
});





export default BoardHashtag;