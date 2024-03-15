import Carousel from 'react-bootstrap/Carousel';
import CarouselCaption from 'react-bootstrap/esm/CarouselCaption';
import CarouselItem from 'react-bootstrap/esm/CarouselItem';
import Container from 'react-bootstrap/esm/Container';
import Image from 'react-bootstrap/Image';

const Home = () => {
    return (
      <>
      <Container className='text-center'>
      <h1>Vanguards</h1>
      <h3>Featuring the best cards in the game:</h3>
      <Carousel className='card-carousel'>
        <CarouselItem className='card-carousel'>
          <Image src="ALP.MEL.001.png" height={750}/>
          <CarouselCaption>
            <h3>Fighter</h3>
            <p>The Best Card in the Game</p>
          </CarouselCaption>
        </CarouselItem>
        <CarouselItem>
          <Image src="ALP.PRM.005.png" height={750}/>
          <CarouselCaption>
            <h3>dog</h3>
            <p>dog</p>
          </CarouselCaption>
        </CarouselItem>
        <CarouselItem>
          <Image src="ALP.ARC.021.png" height={750}/>
          <CarouselCaption>
            <h3>Chain Lightning</h3>
            <p>The Only Way to Beat Melee</p>
          </CarouselCaption>
        </CarouselItem>
        <CarouselItem>
          <Image src="ALP.ARC.034.png" height={750}/>
          <CarouselCaption>
            <h3>Hurricane</h3>
            <p>Anti-dog Weather</p>
          </CarouselCaption>
        </CarouselItem>
      </Carousel>
      </Container>
      </>
    );
  };
  
  export default Home;