import React, { Component } from 'react';
import createClass from 'create-react-class';
import App from './App.css';
import BoardHashtag from './Board';
import Hashtag  from './Hashtag';
import listaHash from './data/listaHash.js';


var SearchBar = createClass({


    getInitialState: function (){
        return {defaultText: 'Type your hashtag..', items: listaHash,
                hashtags: listaHash}
                },


    filterButtons: function (event){
        var updatedList = this.state.hashtags;
        updatedList = updatedList.filter(function (item){
                                            return item.toLowerCase().search(
                                                    event.target.value.toLowerCase()) !== -1;
                                         });
        this.setState({items: updatedList});
    },


    render: function (){
        return (<div className='SearchContainer'>
                    <h3>Choose</h3>
                    <form method="post" action="/hello">
                        <input type="text" placeholder={this.state.defaultText} onChange={this.filterButtons} name='hashtag' />
                    </form>
                    <BoardHashtag inheritState={this.state.items.slice(0,60)} />
                </div>)
    }
});

export default SearchBar;

// Get reference to one of my child: to call ref: variable = this.refs.newHash.value
// when buttons belong to other components: how do we call functions? Properties: you can pass entire function
// to <Hashtag updateText={this.updateComment}>  to recall the function in another function: this.props.NAME_FUNCTION
// the same stands for other properties.