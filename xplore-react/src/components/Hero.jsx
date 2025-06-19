import React from 'react'

const Hero = () => {
  return (
    <>
        <section className='hero-section w-full'>
          <div className='hero-grid'>
            <div className='card card-1'>
              <div className='bg-container'>
                <div className='x-bg'>X</div>
                <div className='p-bg'>P</div>
              </div>
              <div className='card-content'>
                <h2>Your</h2>
                <h2>Future.</h2>
                <h2>Mapped by</h2>
                <h2>XPlore</h2>
                <p>Personalized career guidance, built for the New Gen.</p>
                <div className='cta-link'>More about Xplore</div>
              </div>
              <div className='boy-reading'>
                <img src="/images/reading-boy.png" alt="Reading Boy" />
              </div>
            </div>
            <div className='card card-2'></div>
          </div>
        </section>
    </>
  )
}

export default Hero