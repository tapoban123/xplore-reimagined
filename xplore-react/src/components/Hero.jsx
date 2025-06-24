import React from "react";
import StartBtn from "./StartBtn";

const Hero = () => {
  return (
    <>
      <section className="hero-section w-full">
        <div className="hero-grid">
          <div className="card card-1">
            <div className="bg-container">
              <div className="x-bg">
                <img src="/images/X.png" />
              </div>
              <div className="p-bg">
                <img src="/images/P.png" />
              </div>
            </div>
            <div className="card-content">
              <h2>Your</h2>
              <h2>Future.</h2>
              <h2>Mapped by</h2>
              <h2>XPlore</h2>
              <p>
                Personalized career guidance,
                <br /> built for the New Gen.
              </p>
              <div className="cta-link">More about Xplore</div>
            </div>
            <div className="boy-reading">
              <img src="/images/reading-boy.png" alt="Reading Boy" />
            </div>
          </div>
          <div className="card card-2">
            <div className="card2-content">
              <h2>THIS ISN'T</h2>
              <h2>YOUR</h2>
              <h2>SCHOOL TEST</h2>
            </div>
            <div className="boy-falling">
              <img src="/images/falling-boy.png" alt="Falling Boy" />
            </div>
          </div>
          <div className="card-changed card-3">
            <div className="card3-content">
              <h3>Everyone's figuring out</h3>
              <h3>So are YOU.</h3>
            </div>
            <div className="girl-reading">
              <img src="/images/reading-girl.png" alt="Reading Girl" />
            </div>
          </div>
          <div className="card-changed card-4">
            <div className="card4-content">
              <h4>FAQ</h4>
              <h2>
                See Your Future
                <br /> Through the <br />
                Right Lens
              </h2>
              <p>
                Choose the life you want to capture. We <br />
                help you focus on the right career path.
              </p>
              <div className="camera-girl">
                <img src="/images/camera-girl.png" alt="Camera Girl" />
              </div>
            </div>
          </div>
          <div className="card card-5 flex items-center">
            <StartBtn />
          </div>
          <div className="card card-6">
            <div className="card6-content">
              <h4>AI Chatbot</h4>
              <h1>
                Not Just AI. Your <br />
                Career <br /> Wingman
              </h1>
              <p>
                Ask anything - from what to become, to <br />
                how to become it. No awkward forms. Just <br />
                real answers
              </p>
              <div className="chatbot-img">
                <img src="/images/ai-chatbot.png" alt="Chatbot Image" />
              </div>
            </div>
          </div>
          <div className="card card-7">
            <div className="card7-content">
              <h4>Mobile App</h4>

              <div className="qr-scanner">
                <img
                  className="phone-case"
                  src="/images/phone-case.png"
                  alt="Phone Case"
                />

                <div className="qr-overlay">
                  <h3>
                    Download the Mobile <br /> App now
                  </h3>
                  <img
                    className="qr-img"
                    src="/images/qr-scan.png"
                    alt="QR Code"
                  />
                  <img
                    className="border-img"
                    src="/images/border.png"
                    alt="Border"
                  />
                </div>
              </div>
            </div>
          </div>
          <div className="card card-8">
            <h1 className="tribe-heading">FIND YOUR TRIBE</h1>
            <div className="tribe-img">
              <img src="/images/tribe-image.png" alt="Tribe Illustration" />
            </div>
          </div>
          <div className="card card-9">
            <div className="card9-content">
              <h4>Psychologist Support</h4>
              <h1>Browse certified therapists</h1>
              <p>
                Talk to licensed <br /> psychologists <br /> who get it — from{" "}
                <br /> burnout to <br />
                anxiety
              </p>
            </div>
            <div className="therapist-img">
              <img src="/images/psychologist.png" alt="Therapist" />
            </div>
          </div>
          {/* card-10 */}
          <div className="card card-10">
            <h4>Mentorship</h4>
            <h1>Explore Careers with a Mentor</h1>
            <div className="mentors-list">
              {[
                {
                  name: "Tung Tung Sahur",
                  rating: "★ 4.5",
                  field: "Brainrot",
                  image: "/images/mentor-1.png",
                },
                {
                  name: "Brr Brr Patapin",
                  rating: "★ 4.7",
                  field: "Videography",
                  image: "/images/mentor-2.jpg",
                },
                {
                  name: "Schimpanzini Bananini",
                  rating: "★ 4.5",
                  field: "Animation",
                  image: "/images/mentor-3.png",
                },
              ].map((mentor, idx) => (
                <div className="mentor-card" key={idx}>
                  <img src={mentor.image} alt={mentor.name} />
                  <p className="mentor-name">{mentor.name}</p>
                  <p className="mentor-field">
                    {mentor.rating} | {mentor.field}
                  </p>
                  <button className="mentor-btn">Contact</button>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Hero;
