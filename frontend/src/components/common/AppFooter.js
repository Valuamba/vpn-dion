import React from "react";
import { BackTop} from 'antd'
import { Link} from 'react-router-dom'

function AppFooter() {
    return (
        <div className="fluid-container">
            <div className="footer">
                <div className="logo">
                    <i className="fas fa-home fa-2x"></i>
                    <Link to="/">Real Estate</Link>
                </div>
                <ul className="social-links">
                    <li>
                        <a href="https://www.twitter.com/">
                            <i className="fab fa-twitter"/>
                        </a>
                    </li>
                </ul>
                <BackTop>
                    <div className="goTop">
                        <i className="fab fas-arrow-circle-up"/>
                    </div>
                </BackTop>
            </div>
        </div>
    )
}

export default AppFooter