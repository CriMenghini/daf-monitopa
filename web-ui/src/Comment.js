import React, { Component } from 'react';
import createClass from 'create-react-class';



var Comment = createClass({

    getInitialState: function (){
        return {status: this.props.children}
    },

    edit: function () {
        this.setState({status: 'edit'})
        alert('Editing coming');
    },

    remove: function () {
        this.setState({status: 'remove'})
        alert ('Removing comment');
    },

    render: function (){
        var comment = this.props.children;
        if (this.state.status == 'edit'){
            comment = prompt('Enter your movie', this.props.children)
        }
        else if(this.state.status == 'remove'){
            comment = ''
        }

        return (
                <div className='commentContainer'>
                    <div className='commentText'> {comment} </div>
                    <button onClick={this.edit} className='button-primary'>Edit</button>
                    <button onClick={this.remove} className='button-danger'>Remove</button>
                </div>
        );
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




export default Comment;