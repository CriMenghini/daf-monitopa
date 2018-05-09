import React, { Component } from 'react';
import createClass from 'create-react-class';
import Board from './Board';


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

export default Comment;