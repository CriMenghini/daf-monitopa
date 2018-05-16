import React, { Component } from 'react';
import createClass from 'create-react-class';
import numTweet from './data/numberTweet_hashtag.js';
import Retweet from './data/TopRetweet.js';



var Viz = createClass ({
            //const numTweet = data.NumTweet
//            const NumRetweet = data.NumRetweet
//            const sentence = sentence

            render() {return (<div>
                         <p>{this.props.numtweet}</p>
                         <br />
                         <p>{this.props.numretweet}</p>
                    </div>);}

});

export default Viz;