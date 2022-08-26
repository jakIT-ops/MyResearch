# Condition Variables

Condition variables enable threads to be synchronized via messages. They need the <condition_variable> header, one thread to act as a sender, and the other as the receiver of the message; the receiver waits for the notification from the sender. Typical use cases for condition variables are sender-receiver or producer-consumer workflows.

A condition variable can be the sender but also the receiver of the message.

| Method 	|	Description |
| :------------ | ----------------: |
|cv.notify_one()|Notifies a waiting thread.|
|cv.notify_all()|Notifies all waiting threads.|
|cv.wait(lock, ...)|Waits for the notification while holding a std::unique_lock. |
|cv.wait_for(lock, relTime, ...)|Waits for a time duration for the notification while holding a std::unique_lock.|
|cv.wait_until(lock, absTime, ...)|Waits until a time point for the notification while holding a std::unique_lock.|














