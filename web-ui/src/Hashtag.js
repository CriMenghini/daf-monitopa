import React, { Component } from 'react';
import createClass from 'create-react-class';
import './App.css';
import BoardHashtag from './Board';


var Hashtag = createClass({

        render: function (){
            return (<div className='Hashtag'>
                        <form onSubmit={this.props.funzioneSubmit}>
                            <button className='tag' name='selectedHashtag' value={this.props.children} onClick={this.props.funzioneClick}>#{this.props.children}</button>
                        </form>
                    </div>);
        }
});




export default Hashtag;
