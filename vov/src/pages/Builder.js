import Container from 'react-bootstrap/esm/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

const Builder = () => {
    return (
      <>
      <Container>
        <Row>
          <Col>
            <Container className='card-database-container' fluid>
              Test
            </Container>
          </Col>
          <Col>
            <Container className='current-deck-container'>
              Test
            </Container>
          </Col>
        </Row>
      </Container>
      </>
    )
  };
  
  export default Builder;