package com.snapaction

import android.app.Service
import android.content.Intent
import android.database.ContentObserver
import android.net.Uri
import android.os.Handler
import android.os.IBinder
import android.os.Looper
import android.provider.MediaStore
import android.util.Log
import android.widget.Toast

// 📸 Android Service that listens for new screenshots via ContentObserver
class ScreenshotService : Service() {

    private lateinit var contentObserver: ContentObserver

    override fun onCreate() {
        super.onCreate()
        Log.d("SnapAction", "Service Created")
        
        // Listen to the MediaStore for new images
        contentObserver = object : ContentObserver(Handler(Looper.getMainLooper())) {
            override fun onChange(selfChange: Boolean, uri: Uri?) {
                super.onChange(selfChange, uri)
                if (uri != null) {
                    handleNewScreenshot(uri)
                }
            }
        }

        contentResolver.registerContentObserver(
            MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
            true,
            contentObserver
        )
    }

    private fun handleNewScreenshot(uri: Uri) {
        Log.i("SnapAction", "📸 New Screenshot detected: $uri")
        
        // In a real app, we would:
        // 1. Read the Bitmap from URI
        // 2. Pass to Gemini Nano (On-Device) or TFLite model
        // 3. Show a floating Bubble/Overlay (WindowManager)
        
        // Simulation for MVP:
        Toast.makeText(this, "SnapAction: Analyzing Intent... 🧠", Toast.LENGTH_SHORT).show()
        
        // Mocking the analysis result
        analyzeImage(uri)
    }
    
    private fun analyzeImage(uri: Uri) {
        // TODO: Call local LLM here
        // val result = LocalLLM.inference(bitmap)
        
        val mockIntent = "SHOPPING" // Detected intent
        showCapsule(mockIntent, "🔍 Find Best Price")
    }
    
    private fun showCapsule(intentType: String, label: String) {
        Log.d("SnapAction", "🔮 Intent: $intentType | Label: $label")
        // TODO: Draw UI using WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY
    }

    override fun onBind(intent: Intent?): IBinder? {
        return null
    }

    override fun onDestroy() {
        super.onDestroy()
        contentResolver.unregisterContentObserver(contentObserver)
    }
}
