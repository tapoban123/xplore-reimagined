import React from 'react'

const Hero = () => {
  return (
    <>
        <section className='hero-section w-full'>
          <div className='hero-grid'>
            <div className='card card-1'>
              <div className='bg-container'>
                <div className='x-bg'><img src='/images/X.png'/></div>
                <div className='p-bg'><img src='/images/P.png'/></div>
              </div>
              <div className='card-content'>
                <h2>Your</h2>
                <h2>Future.</h2>
                <h2>Mapped by</h2>
                <h2>XPlore</h2>
                <p>Personalized career guidance,<br/> built for the New Gen.</p>
                <div className='cta-link'>More about Xplore</div>
              </div>
              <div className='boy-reading'>
                <img src="/images/reading-boy.png" alt="Reading Boy" />
              </div>
            </div>
            <div className='card card-2'>
              <div className='card2-content'>
                <h2>THIS ISN'T</h2>
                <h2>YOUR</h2>
                <h2>SCHOOL TEST</h2>
              </div>
              <div className='boy-falling'>
                <img src="/images/falling-boy.png" alt="Falling Boy" />
              </div>
            </div>
            <div className='card-changed card-3'>
              <div className='card3-content'>
                <h3>Everyone's figuring out</h3>
                <h3>So are YOU.</h3>
              </div>
              <div className='girl-reading'>
                <img src="/images/reading-girl.png" alt="Reading Girl" />
              </div>
            </div>
            <div className='card-changed card-4'>
              <div className='card4-content'>
                <h4>FAQ</h4>
                <h2>See Your Future<br/> Through the <br />Right Lens</h2>
                <p>Choose the life you want to capture. We <br />help you focus on the right career path.</p>
                <div className='camera-girl'>
                  <img src="/images/camera-girl.png" alt="Camera Girl" />
                </div>
              </div>
            </div>
            <div className='card card-5 '></div>
              
          </div>
        </section>
    </>
  )
}

export default Hero