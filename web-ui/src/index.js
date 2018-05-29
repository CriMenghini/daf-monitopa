import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import './App.css';
import registerServiceWorker from './registerServiceWorker';
import createClass from 'create-react-class';
import Comment from './Comment';
import BoardHashtag from './Board';
import Hashtag  from './Hashtag';
import SearchBar from './SearchBar';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';
import HomePage from './HomePage';



var LandingPage = createClass({

    getInitialState: function (){
        return {choice: false}
    },


    handleChoice: function (){
        this.setState({choice: !this.state.choice})
    },




    render: function (){

            if (this.state.choice){
                return (<App {... this.props} {... this.state} scegliAnalisi={this.handleChoice}/>)
            }
            else {
                return (<HomePage {... this.props} {... this.state} scegliAnalisi={this.handleChoice}/>)
            };


    }


});



ReactDOM.render(<LandingPage />, document.getElementById('root'));
registerServiceWorker();
