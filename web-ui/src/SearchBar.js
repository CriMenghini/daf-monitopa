import React, { Component } from 'react';
import createClass from 'create-react-class';
import './Hashtag.css';
import BoardHashtag from './Board';
import Hashtag  from './Hashtag';


var SearchBar = createClass({


    getInitialState: function (){
        return {defaultText: 'Type your hashtag..'}
    },


    render: function (){
        return (<div className='SearchContainer'>
                    <h1>Build Search Bar</h1>
                    <form method="post" action="/hello">
                        <input type="text" placeholder={this.state.defaultText} name='hashtag'></input>
                        <button type="submit">Search</button>
                    </form>
                </div>)
    }
});

export default SearchBar;