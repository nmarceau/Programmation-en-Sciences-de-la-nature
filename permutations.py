{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "39916800\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[11], line 10\u001b[0m\n\u001b[0;32m      8\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m alignements[i][\u001b[38;5;241m0\u001b[39m] \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m21\u001b[39m: \n\u001b[0;32m      9\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m alignements[i][\u001b[38;5;241m8\u001b[39m] \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m8\u001b[39m \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;241m8\u001b[39m \u001b[38;5;129;01min\u001b[39;00m alignements[i] \u001b[38;5;241m==\u001b[39m \u001b[38;5;28;01mFalse\u001b[39;00m :\n\u001b[1;32m---> 10\u001b[0m             possible\u001b[38;5;241m.\u001b[39mappend(alignements[i])\n\u001b[0;32m     12\u001b[0m \u001b[38;5;28mprint\u001b[39m(possible)\n",
      "Cell \u001b[1;32mIn[11], line 10\u001b[0m\n\u001b[0;32m      8\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m alignements[i][\u001b[38;5;241m0\u001b[39m] \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m21\u001b[39m: \n\u001b[0;32m      9\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m alignements[i][\u001b[38;5;241m8\u001b[39m] \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m8\u001b[39m \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;241m8\u001b[39m \u001b[38;5;129;01min\u001b[39;00m alignements[i] \u001b[38;5;241m==\u001b[39m \u001b[38;5;28;01mFalse\u001b[39;00m :\n\u001b[1;32m---> 10\u001b[0m             possible\u001b[38;5;241m.\u001b[39mappend(alignements[i])\n\u001b[0;32m     12\u001b[0m \u001b[38;5;28mprint\u001b[39m(possible)\n",
      "File \u001b[1;32m_pydevd_bundle/pydevd_cython.pyx:1457\u001b[0m, in \u001b[0;36m_pydevd_bundle.pydevd_cython.SafeCallWrapper.__call__\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32m_pydevd_bundle/pydevd_cython.pyx:701\u001b[0m, in \u001b[0;36m_pydevd_bundle.pydevd_cython.PyDBFrame.trace_dispatch\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32m_pydevd_bundle/pydevd_cython.pyx:1152\u001b[0m, in \u001b[0;36m_pydevd_bundle.pydevd_cython.PyDBFrame.trace_dispatch\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32m_pydevd_bundle/pydevd_cython.pyx:1135\u001b[0m, in \u001b[0;36m_pydevd_bundle.pydevd_cython.PyDBFrame.trace_dispatch\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32m_pydevd_bundle/pydevd_cython.pyx:312\u001b[0m, in \u001b[0;36m_pydevd_bundle.pydevd_cython.PyDBFrame.do_wait_suspend\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32mc:\\Users\\nelson\\anaconda3\\Lib\\site-packages\\debugpy\\_vendored\\pydevd\\pydevd.py:2070\u001b[0m, in \u001b[0;36mPyDB.do_wait_suspend\u001b[1;34m(self, thread, frame, event, arg, exception_type)\u001b[0m\n\u001b[0;32m   2067\u001b[0m             from_this_thread\u001b[38;5;241m.\u001b[39mappend(frame_custom_thread_id)\n\u001b[0;32m   2069\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_threads_suspended_single_notification\u001b[38;5;241m.\u001b[39mnotify_thread_suspended(thread_id, thread, stop_reason):\n\u001b[1;32m-> 2070\u001b[0m         keep_suspended \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_do_wait_suspend(thread, frame, event, arg, suspend_type, from_this_thread, frames_tracker)\n\u001b[0;32m   2072\u001b[0m frames_list \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   2074\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m keep_suspended:\n\u001b[0;32m   2075\u001b[0m     \u001b[38;5;66;03m# This means that we should pause again after a set next statement.\u001b[39;00m\n",
      "File \u001b[1;32mc:\\Users\\nelson\\anaconda3\\Lib\\site-packages\\debugpy\\_vendored\\pydevd\\pydevd.py:2106\u001b[0m, in \u001b[0;36mPyDB._do_wait_suspend\u001b[1;34m(self, thread, frame, event, arg, suspend_type, from_this_thread, frames_tracker)\u001b[0m\n\u001b[0;32m   2103\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_call_input_hook()\n\u001b[0;32m   2105\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprocess_internal_commands()\n\u001b[1;32m-> 2106\u001b[0m     time\u001b[38;5;241m.\u001b[39msleep(\u001b[38;5;241m0.01\u001b[39m)\n\u001b[0;32m   2108\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcancel_async_evaluation(get_current_thread_id(thread), \u001b[38;5;28mstr\u001b[39m(\u001b[38;5;28mid\u001b[39m(frame)))\n\u001b[0;32m   2110\u001b[0m \u001b[38;5;66;03m# process any stepping instructions\u001b[39;00m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
