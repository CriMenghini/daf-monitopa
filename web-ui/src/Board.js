import React, { Component } from 'react';
import createClass from 'create-react-class';
import Comment from './Comment';
import Hashtag  from './Hashtag';
import './Hashtag.css';


var BoardHashtag = createClass({

    getInitialState: function (){
        return {items: this.props.inheritState}
    },

    eachHashtag: function (text, i){
        return (<Hashtag key={i} index={i}>
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