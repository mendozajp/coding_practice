import { useState, useEffect } from 'react';
import './countdown.css';

const CountdownTimer = () => {
    const [timeStarted, setStartTime] = useState(false);
    const [hour, setHour] = useState(0);
    const [minute, setMinute] = useState(0);
    const [second, setSecond] = useState(0);
    const [allowNotifications, changeNotificationPermissions] = useState(false)
    const [askPermissionsBlocker, setPersmissionBlocker] = useState(false)

    const askNotifcationPermissions = () => {
        if (askPermissionsBlocker){
            return;
        }
        if (Notification.permission === "granted") {
            changeNotificationPermissions(true)
            setPersmissionBlocker(true)
            return;
        }
        if (!("Notification" in window)) {
            console.log("this browser does not support notifcations")
            setPersmissionBlocker(true)
            return;
        }
        Notification.requestPermission().then((result) => {
            if (result === "granted") {
                changeNotificationPermissions(true)
                setPersmissionBlocker(true)
                return;
            }
            else {
                // permissions were denied. block asking again.
                setPersmissionBlocker(true)
            }
        })
    }

    useEffect(() => {
        if (!timeStarted){
            return;
        }
        const timer = setTimeout(() => {
                moveTime()
            }, 1000);
        return () => clearTimeout(timer)
    });

    const Pause = () => {
        setStartTime(false);
        return;
    }

    const Reset = () => {
        async function resetTime() {
            setStartTime(false);
            setHour(0);
            setMinute(0);
            setSecond(0);
            return;
        }
        resetTime()
    }

    const Start = () => {
        askNotifcationPermissions()
        setStartTime(true);
        return;
    }

    const moveTime = () => {
        if (hour > 0 || minute > 0 || second > 0) {
            if (second === 0) {
                // attempt to decrement minutes
                if (minute === 0){
                    // attempt to decrement hours, 
                    // if hour is 0, you should never get this far
                    setHour(hour - 1)
                    setMinute(59)
                }
                else {
                    setMinute(minute - 1)
                }
                setSecond(59)
            }
            else{
                setSecond(second - 1)
            }
        }
        else {
            //you're done, do whatever notification logic here
            if (allowNotifications) {
                new Notification("Timer Done!", {body:"Timer Done!"})
            }
            return;
        }
    }

    /// Component that allows entering times for countdown. Converts when start is hit
    const InputTimer = () => {
        return (
            <div className='inputWrapper'>
                <input className="genericInput" value={hour} onChange={e => setHour(Number(e.target.value))}/>
                <b> : </b>
                <input className="genericInput" value={minute} onChange={e => setMinute(Number(e.target.value))}/>
                <b> : </b>
                <input className="genericInput" value={second} onChange={e => setSecond(Number(e.target.value))}/>
                <button className="genericButton" onClick={Start}>Start</button>
            </div>
        )
    }

    /// Counting down timer component once started. Inputs gone, values decrement
    const OutputTimer = () => {
        return (
            <div className='inputWrapper'>
                <b> {hour} </b>
                <b> : </b>
                <b> {minute} </b>
                <b> : </b>
                <b> {second} </b>
                <button className="genericButton" onClick={Pause}>Pause</button>
                <button className="genericButton" onClick={Reset}>Reset</button>
            </div>
        )
    }


    const Timer = () => {
        return timeStarted ? OutputTimer() : InputTimer()
    }

    return (
        <div>
            <Timer />
        </div>
    )

}


export default CountdownTimer;