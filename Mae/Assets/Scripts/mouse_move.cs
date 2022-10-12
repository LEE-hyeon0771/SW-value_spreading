using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class mouse_move : MonoBehaviour
{
    public Transform mouse;
    private Vector3 curr_pos;
    public GameObject Shoot;
    bool is_shoot = false;
    private float period = 0;

    // Start is called before the first frame update
    void Start()
    {
      
    }

    // Update is called once per frame
    void Update()
    {
        curr_pos.x = Input.mousePosition.x;
        curr_pos.y = Input.mousePosition.y;
        curr_pos.z = (float)-1.5;
        mouse.position = curr_pos;

        if (Input.GetMouseButtonDown(0))
        {
            Shoot.SetActive(true);
            Shoot.transform.position = curr_pos;
            is_shoot = true;
        }
        if (is_shoot)
        {
            period += Time.deltaTime;
            if (period > 0.3)
            {
                period = 0;
                Shoot.SetActive(false);
            }
        }
    }
}
