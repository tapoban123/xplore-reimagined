import React, { useState, useRef, useEffect } from "react";



const StartBtn = () => {
  const [isDragging, setIsDragging] = useState(false);
  const [dragProgress, setDragProgress] = useState(0);
  const [isCompleted, setIsCompleted] = useState(false);
  const containerRef = useRef(null);
  const sliderRef = useRef(null);

  



  const handleMouseDown = (e) => {
    if (isCompleted) return;
    setIsDragging(true);
    e.preventDefault();
  };

  const handleMouseMove = (e) => {
    if (!isDragging || isCompleted || !containerRef.current) return;
    const containerRect = containerRef.current.getBoundingClientRect();
    const sliderWidth = 80;
    const maxDrag = containerRect.width - sliderWidth;
    let newX = e.clientX - containerRect.left - sliderWidth / 2;
    newX = Math.max(0, Math.min(newX, maxDrag));
    const progress = newX / maxDrag;
    setDragProgress(progress);
    if (progress > 0.8) {
      setIsCompleted(true);
      setIsDragging(false);
      setDragProgress(1);
    }
  };

  const handleMouseUp = () => {
    if (!isCompleted) setDragProgress(0);
    setIsDragging(false);
  };

  const handleTouchStart = (e) => {
    if (isCompleted) return;
    setIsDragging(true);
    e.preventDefault();
  };

  const handleTouchMove = (e) => {
    if (!isDragging || isCompleted || !containerRef.current) return;
    const touch = e.touches[0];
    const containerRect = containerRef.current.getBoundingClientRect();
    const sliderWidth = 80;
    const maxDrag = containerRect.width - sliderWidth;
    let newX = touch.clientX - containerRect.left - sliderWidth / 2;
    newX = Math.max(0, Math.min(newX, maxDrag));
    const progress = newX / maxDrag;
    setDragProgress(progress);
    if (progress > 0.8) {
      setIsCompleted(true);
      setIsDragging(false);
      setDragProgress(1);
    }
  };

  const handleTouchEnd = () => {
    if (!isCompleted) setDragProgress(0);
    setIsDragging(false);
  };

  useEffect(() => {
    if (isDragging) {
      document.addEventListener("mousemove", handleMouseMove);
      document.addEventListener("mouseup", handleMouseUp);
      document.addEventListener("touchmove", handleTouchMove, { passive: false });
      document.addEventListener("touchend", handleTouchEnd);
    }
    return () => {
      document.removeEventListener("mousemove", handleMouseMove);
      document.removeEventListener("mouseup", handleMouseUp);
      document.removeEventListener("touchmove", handleTouchMove);
      document.removeEventListener("touchend", handleTouchEnd);
    };
  }, [isDragging]);

  const maxDragDistance = containerRef.current
    ? containerRef.current.offsetWidth - 80
    : 320;

  const ArrowRight = () => (
    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 12h14"></path>
      <path d="M12 5l7 7-7 7"></path>
    </svg>
  );

  const Check = () => (
    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
      <path d="M20 6L9 17l-5-5"></path>
    </svg>
  );

  // Determine if progress has passed the threshold (to align text to right)
  const shiftRight = dragProgress >= 0.35;

  return (
    <div
      ref={containerRef}
      className="relative h-[86px] w-full rounded-full overflow-hidden cursor-pointer select-none transition-all duration-300"
      style={{
        backgroundColor: isCompleted ? "#20BC20" : "#ffffff",
      }}
    >
      {/* Fill Progress */}
      <div
        className="absolute top-0 left-0 h-full rounded-full transition-all duration-200"
        style={{
          width: `${dragProgress * 100}%`,
          backgroundColor: "rgba(32, 188, 32, 0.2)",
          opacity: dragProgress > 0 ? 1 : 0,
        }}
      />

      {/* Text */}
      <div
        className={`absolute inset-0 flex items-center transition-all duration-500 ease-in-out ${
          shiftRight ? "justify-end pr-[100px]" : "justify-start pl-[100px]"
        }`}
      >
        <span
          className="journey-text transition-all duration-500"
          style={{
            color: isCompleted ? "#FFFFFF" : "#757373",
            fontSize: "6.3rem",
            fontWeight: 400,
            textTransform: "uppercase",
            fontFamily: "Heathergreen, sans-serif",
            letterSpacing: "0.01em",
            whiteSpace: "nowrap",
          }}
        >
          {isCompleted ? "THERE YOU GO" : "START YOUR JOURNEY NOW"}
        </span>
      </div>

      {/* Slider Button */}
      <div
        ref={sliderRef}
        className="absolute top-1 left-1 h-[78px] w-[78px] rounded-full flex items-center justify-center shadow-lg cursor-grab active:cursor-grabbing transition-all duration-200 z-10"
        style={{
          transform: `translateX(${dragProgress * maxDragDistance}px)`,
          transition: isDragging ? "none" : "transform 0.3s ease",
          backgroundColor: isCompleted ? "#000000" : "#000000",
        }}
        onMouseDown={handleMouseDown}
        onTouchStart={handleTouchStart}
      >
        <div className="text-white">
          {isCompleted ? <Check /> : <ArrowRight />}
        </div>
        
      </div>
    </div>
  );
};

export default StartBtn;