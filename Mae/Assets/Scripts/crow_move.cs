using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class crow_move : MonoBehaviour
{
    public float s_point = 1;
    private float x_pos = 0;
    private float y_pos = 0;
    private float period = 0;

    public Transform falcon;
    Vector2 curr_pos;
    Quaternion curr_rot;
    bool isturn = false;
    private Vector2 initial_pos;

    // Start is called before the first frame update
    void Start()
    {
        period = 0;
        curr_pos = falcon.position;
        initial_pos = falcon.position;
    }

    // Update is called once per frame
    void Update()
    {
        period += Time.deltaTime;
        x_pos = Mathf.Sin(-period + s_point);
        y_pos = Mathf.Cos(-s_point + 2 * period);
        curr_pos.x = initial_pos.x + x_pos * 100;
        curr_pos.y = initial_pos.y + y_pos * 50;
        falcon.position = curr_pos;

        

        if (!isturn)
        {
            if (x_pos < -0.95)
            {
                isturn = true;
                curr_rot.y = curr_rot.y - 180;
                falcon.rotation = curr_rot;
            }
        }
        else
        {
            if (x_pos > 0.95) { 
                isturn = false;
                curr_rot.y = curr_rot.y + 180;
                falcon.rotation = curr_rot;
            }

        }
    }
}
