import React from "react"
import './App.css';
import AppHeader from "./components/common/AppHeader";
// import { AppFooter } from "./components/common/AppFooter";
import { Layout } from "antd";
import HomePage from "./pages/HomePage";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Alert } from "antd";
import PropertyListPage from "./pages/PropertyList";
import PaymentPage from "./pages/Payment"

const { Content, Header, Footer } = Layout


// function App() {
// 	return (
//     <AppHeader/>
//   )
// }

function App() {
  return (
    <Router>
      <Layout className="main-layout">
        <Header>
            <AppHeader/>
        </Header>
        <Content>
            <Routes>
              <Route exact path="/some" component={HomePage}></Route>
              <Route path="/" element={<HomePage/>}></Route>
              <Route path="/properties" element={<PropertyListPage/>}></Route>
              <Route path="/payment" element={<PaymentPage/>}></Route>
            </Routes>
        </Content>
        {/* <Footer>
            <AppFooter/>
        </Footer> */}
      </Layout>
    </Router>
  );
}

export default App;
