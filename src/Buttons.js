import React from 'react';

class Buttons extends React.Component {
    // Function to handle button clicks
    handleButtonClick = (buttonText) => {
        alert(`Action "${buttonText}"!`);
    }

    render() {
        return (
            <div>
                <button onClick={() => this.handleButtonClick('See location')}>See location</button>
                <button onClick={() => this.handleButtonClick('Device available')}>Device available</button>
                <button onClick={() => this.handleButtonClick('Connection')}>Connection</button>
            </div>
        );
    }
}

export default Buttons;