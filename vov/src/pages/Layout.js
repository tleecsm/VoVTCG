import { Outlet, Link } from "react-router-dom";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import NavbarCollapse from "react-bootstrap/esm/NavbarCollapse";
import Image from 'react-bootstrap/Image';

const Layout = () => {
  return (
    <>
      <Navbar className="bg-dark-subtle">
        <Container className="align-items-center">
          <Navbar.Brand href="/">
          <Image src="logosmall.png" className="layout-image"></Image>
          <text>Vanguards</text>
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav>"></Navbar.Toggle>
          <NavbarCollapse id="responsive-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/builder">
                Deck Builder
              </Nav.Link>
              <Nav.Link href="/database">
                Card Database
              </Nav.Link>
            </Nav>
            <Nav>
              <NavDropdown title="Username">
                <NavDropdown.Item href="#">Logout</NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </NavbarCollapse>
        </Container>
      </Navbar>

      <Outlet />
    </>
  )
};

export default Layout;