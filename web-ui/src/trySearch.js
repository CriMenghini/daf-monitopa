import React, { Component } from 'react';
import createClass from 'create-react-class';


var Search = createClass ({
            //const numTweet = data.NumTweet
//            const NumRetweet = data.NumRetweet
//            const sentence = sentence

            render() {return (<div id="signup">
                        <form onSubmit={this.props.funzioneSubmit}>
                            <button className='tag' name='selectedHashtag' value='renzi' onClick={this.props.funzioneClick}>renzi</button>

                        </form>
                    </div>);}

});

export default Search;


