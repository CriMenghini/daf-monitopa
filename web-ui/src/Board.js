import React, { Component } from 'react';
import createClass from 'create-react-class';
import Comment from './Comment';
import Hashtag  from './Hashtag';
import './Hashtag.css';


var BoardHashtag = createClass({

    getInitialState: function (){
        return {hashtags: ['astori',
                           'africa',
                           'elezioni',
                           'calcio',
                           'toscana']}
    },

    eachHashtag: function (text, i){
        return (<Hashtag key={i} index={i}>
                    {text}
                </Hashtag>
           );

    },

    render: function (){
        return (<div className='boardHash'>
                    {this.state.hashtags.map(this.eachHashtag)}
                </div>)
    }
});



var Board = createClass({

    getInitialState: function (){
        return {
            comments: ['i love pizza',
                        'i love bacon',
                         'i love pane']
        }
    },


    removeComment: function (i){
        var arr = this.state.comments;
        arr.splice(i, 1);
        this.setState({comments: arr})
    },

    updateComment: function (newText, i){
        var arr = this.state.comments;
        arr[i] = newText
    },

    eachComment: function (text, i){
                            return (
                            <Comment key={i} index={i}>
                                {text}
                            </Comment>
                            );
                        },

    render: function (){
        return (<div className='board'>
                    {
                        this.state.comments.map(this.eachComment)
                    }

                </div>)
    }


});


export default BoardHashtag;